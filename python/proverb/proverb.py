def proverb(*args, qualifier=None):
    output_text = []
    loop = 0
    while loop < len(args) - 1:
        output_text.append(f"For want of a {args[loop]} the {args[loop+1]} was lost.")
        loop += 1

    if len(args) > 0:
        end = f"{qualifier} {args[0]}" if qualifier else args[0]
        output_text.append(f"And all for the want of a {end}.")
    return output_text
