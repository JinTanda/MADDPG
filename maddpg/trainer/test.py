import sys

def main(argv):
  # このコードは引数と標準出力を用いたサンプルコードです。
  # このコードは好きなように編集・削除してもらって構いません。
  # ---
  # This is a sample code to use arguments and outputs.
  # Edit and remove this code as you like.

  for i, n in enumerate(argv):
    max_cnt = 1
    ans = ""
    n_len = len(n)
    for i in range(1,n_len-1):
      cnt = 0
      for j in range(1,min(i+1,n_len-i)):
        if n[i-j] == n[i+j]:
          cnt += 1
        else:
          break
      if max_cnt < cnt:
        max_cnt = cnt 
        ans = n[i-cnt:i+cnt+1]
    print(ans)

if __name__ == '__main__':
  main(sys.argv[1:])
