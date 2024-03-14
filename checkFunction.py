
def checkPhising(s1, s2):
    m = len(s1)
    n = len(s2)

    # Tạo bảng để lưu độ dài của LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Xây dựng bảng dp
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Truy vết để tìm chuỗi con chung (LCS)
    i, j = m, n
    delChars = []
    addChars = []

    while i > 0 or j > 0:
        if i > 0 and j > 0 and s1[i - 1] == s2[j - 1]:
            i -= 1
            j -= 1
        elif j > 0 and (i == 0 or dp[i][j - 1] >= dp[i - 1][j]):
            addChars.append(s2[j - 1])
            j -= 1
        else:
            delChars.append(s1[i - 1])
            i -= 1

    

    return max(len(addChars), len(delChars)) < max(m,n) / 5 #sửa hệ số này


print(checkPhising('youtube.com','youcute.com'))