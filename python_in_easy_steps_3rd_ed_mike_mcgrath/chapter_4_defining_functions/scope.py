# This is a global variabe. The whole script can access it.
global_var = 1

def my_vars():
    # This is a local variable. In this case only the function has access to it.
    local_var = 2

    # This is a coerced global variable. It is inside the function but now can be accessed anywhere in the script.
    global coerced_global
    coerced_global = 3

    print("Global Variable:", global_var)
    print("Local Variable:", local_var)

my_vars()
print("Coerced Global:",coerced_global)