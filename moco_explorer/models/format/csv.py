from .base import BaseFormatter
import click
import json


class CsvFormatter(BaseFormatter):

    def _sort_header_keys(self, header_keys):
        """
        Sorts the header keys of the csv file by importance

        :param header_keys: The original keys array
        :return: The sorted keys array
        """
        high_importance_keys = ["id", "identifier", "name", "title"]
        low_importance_keys = ["info", "note", "created_at", "updated_at"]

        new_header_keys = []

        for important_key in high_importance_keys:
            if important_key in header_keys:
                new_header_keys.append(important_key)

        other_keys = [x for x in header_keys if x not in high_importance_keys and x not in low_importance_keys]
        other_keys = sorted(other_keys)

        # extract prefixes
        prefixes = []
        for other_key in other_keys:
            if "." in other_key:
                prefix = ".".join(other_key.split(".")[:-1])
                if prefix not in prefixes:
                    prefixes.append(prefix)

        # extract sublists
        for prefix in prefixes:
            # remove the prefix from the sublist and sort it

            # extract the sublist
            sublist = self._sort_header_keys( # get all that start with prefix and when the prefix is replaced contain only one dot
                [x.split(".")[-1] for x in other_keys if x.startswith(prefix) and len(x.replace(prefix, "").split(".")) == 2])
            # eg. when we have a sublist in a sublist
            #
            # customer.name -> will be in customer sublist
            # customer.user.lastname -> will be in customer.user sublist

            # remove the items from the sublist from the other_keys list
            sublist = ["{}.{}".format(prefix, x) for x in sublist]
            other_keys = [x for x in other_keys if x not in sublist]
            other_keys.extend(sublist)

        new_header_keys.extend(other_keys)

        for not_important_key in low_importance_keys:
            if not_important_key in header_keys:
                new_header_keys.append(not_important_key)

        return new_header_keys

    def format_single(self, item):
        return self.format_list([item])

    def format_list(self, items):
        flat_items = []
        header_keys = []
        for item in items:
            dict_item = self.obj_to_dict(item)
            flat_dic = self.flatten_dict(dict_item)

            header_keys.extend([x for x in flat_dic.keys() if x not in header_keys])
            flat_items.append(flat_dic)

        header_keys = self._sort_header_keys(header_keys)

        header = []
        body = []

        for i in range(0, len(flat_items)):
            body.append([])

        for key in header_keys:
            header.append(key)

            for i in range(0, len(flat_items)):
                if key in flat_items[i].keys():
                    body[i].append(flat_items[i][key])
                else:
                    body[i].append("")

        header_line = ";".join(header)
        body_lines = "\n".join([";".join(x) for x in body])
        click.echo(header_line)
        click.echo(body_lines)

    def obj_to_dict(self, obj):
        dict_item = obj
        if hasattr(obj, '__dict__'):
            dict_item = obj.__dict__

            if "custom_properties" in dict_item.keys():
                del dict_item["custom_properties"]

            for key, value in dict_item.items():

                if hasattr(value, '__dict__'):
                    dict_item[key] = self.obj_to_dict(value)

                if isinstance(value, list):
                    dict_item_list = []
                    for value_item in value:
                        dict_item_list.append(self.obj_to_dict(value_item))

                    dict_item[key] = dict_item_list

        return dict_item

    def flatten_dict(self, item, prefix=""):
        tuple_list = []

        for key, value in item.items():
            if isinstance(value, dict):
                new_prefix = ".".join([x for x in [prefix, key] if x != ""])

                tuple_list.extend(
                    self.flatten_dict(value, new_prefix)
                )
            elif isinstance(value, list):
                pass  # no lists
            else:
                flat_key = ".".join(x for x in [prefix, key] if x != "")
                tuple_list.append(
                    (flat_key, value)
                )

        if prefix == "":
            flat_dic = {}
            for key, value in tuple_list:
                flat_dic[key] = str(value).strip().replace(";", "").replace(",", ""). \
                    replace("\r", "\n").replace("\n", ",").replace(",,", ", ")

            return flat_dic

        return tuple_list


