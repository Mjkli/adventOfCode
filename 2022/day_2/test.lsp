(defvar rock 1)
(defvar paper 2)
(defvar sissors 3)
(defvar loss 0)
(defvar draw 3)
(defvar win 6)
(defvar total_1 0)
(defvar total_2 0)

(defun tictoe ( n1 n2 )
    (case n1
        ('a (case n2
                ('x (return-from tictoe (+ draw rock)))
                ('y (return-from tictoe (+ win paper)))
                ('z (return-from tictoe (+ loss sissors)))
        ))
        ('b (case n2
                ('x (return-from tictoe (+ loss rock)))
                ('y (return-from tictoe (+ draw paper)))
                ('z (return-from tictoe (+ win sissors)))
        ))
        ('c (case n2
                ('x (return-from tictoe (+ win rock)))
                ('y (return-from tictoe (+ loss paper)))
                ('z (return-from tictoe (+ draw sissors)))
        ))
    )
)

(defun part2 (n1 n2)
    (case n1
        ('a (case n2
                ('x (return-from part2 (+ loss sissors)))
                ('y (return-from part2 (+ draw rock)))
                ('z (return-from part2 (+ win paper)))
        ))
        ('b (case n2
                ('x (return-from part2 (+ loss rock)))
                ('y (return-from part2 (+ draw paper)))
                ('z (return-from part2 (+ win sissors)))
        ))
        ('c (case n2
                ('x (return-from part2 (+ loss paper)))
                ('y (return-from part2 (+ draw sissors)))
                ('z (return-from part2 (+ win rock)))
        ))
    )
)

(let ((in (open "~/test_input.txt" :if-does-not-exist nil)))
   (when in
      (loop for line = (read-line in nil)
        ;while line do (format t "~a~%" (char (string line)0))
        (incf total_1 (tictoe (format t "~a~%" (char (string line)0) (format t "~a~%" (char (string line)2)))))
        (incf total_2 (part2 (format t "~a~%" (char (string line)0) (format t "~a~%" (char (string line)2)))))
        ;while line do (format t "~a~%" (char (string line)2)))
        (terpri)
      (close in)
      )
    )
)

(write total_1)
(write total_2)
