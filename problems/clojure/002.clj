(def fib
  (lazy-cat [0 1] (map + (rest fib) fib)))

(println (reduce + (filter even? (take-while #(< %1 4000000) fib))))