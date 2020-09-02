import random
def main():
   #print("Keep it logically awesome.")

  f = open("/Users/suyash/Downloads/python-random-quote-master/quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  main()
