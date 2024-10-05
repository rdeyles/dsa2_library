def test(check):
    n=4
    while len(check)<4:
        check.append(n)
        n=n+1
    print(check)

che=[7]
test(che)
