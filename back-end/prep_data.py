def prep_data_f(messages, query, system):
    new_list_messages = []
    i = 0
    for content in messages:
        role = "assistant"
        if i % 2 == 0:
            role = "user"
        obj = {"role": role, "content": content}
        new_list_messages.append(obj)
        i += 1
    query_obj = {"role": "user", "content": query}
    system_obj = {"role": "system", "content": system}
    new_list_messages.insert(0, system_obj)
    new_list_messages.append(query_obj)
    return new_list_messages