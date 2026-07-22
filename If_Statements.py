is_female = False
is_tall = False
if is_female and is_tall:
    print("Female or tall or both")
elif is_female and not(is_tall):
    print("Short Female");
elif not(is_female) and is_tall:
    print("Not female but tall")
else:
    print("Neither a female nor tall")

# try replacing or with and, and observe the output