def find_common_participants(first_group, second_group, delimiter=','):
    first_group_split = first_group.split(delimiter)
    second_group_split = second_group.split(delimiter)
    common_group = list(set(first_group_split).intersection(second_group_split))
    return sorted(common_group)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, delimiter='|'))
