while True:
    try:
        SN = input().strip()
        if not SN:
            break
        print(SN)
    except EOFError:
        break