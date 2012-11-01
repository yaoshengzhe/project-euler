(defn mod3or5? [num]
  (cond (= 0 (mod num 3)) 1
        (= 0 (mod num 5)) 0))

(println (reduce + (filter mod3or5? (take 1000 (range)))))