#Allows us to store info in the form of key value pairs. Access info via key
# Analog to dicitionary to get the definition we access the word first
# give it a name
# All keys to be unique. No duplicate keys
month_Conversions={
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec":"December"
}
# KEEP THIS IN MIND: LIST: [], TUPLE: (), DICTIONARY: {}

print(month_Conversions["Nov"])
print(month_Conversions.get("Dec"))
print(month_Conversions.get("Luv"))
print(month_Conversions.get("Luv","Not a valid key"))
# Key need not be String. It can be a number too.