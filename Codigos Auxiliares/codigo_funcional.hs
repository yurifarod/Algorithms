multiplica x1 x2 =  x1 * x2

fatorial :: Integer -> Integer
fatorial 0 = 1
fatorial n | n > 0 = n * fatorial (n - 1)
           | otherwise = error "Fatorial não definido para números negativos"

multSomas :: Int -> Int -> Int
multSomas a 0 = 0
multSomas a b = a + multSomas a (b - 1)

divSub :: Int -> Int -> Int
divSub a 1 = a
divSub a b | a >= b = 1 + divSub (a-b) b
           | otherwise = 0

dobro x = x * 2

main = do
  print(3*5)
  print(multiplica 10 5)
  print(fatorial 4)
  print(dobro 5)
  print(multSomas 5 4)
  print(divSub 133 5)