def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


use_information = build_profile('yaswanth', 'tanniru', qualification='b.tech', college='bvrit')
print(use_information)