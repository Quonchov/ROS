;; Auto-generated. Do not edit!


(when (boundp 'new_code::WordCount)
  (if (not (find-package "NEW_CODE"))
    (make-package "NEW_CODE"))
  (shadow 'WordCount (find-package "NEW_CODE")))
(unless (find-package "NEW_CODE::WORDCOUNT")
  (make-package "NEW_CODE::WORDCOUNT"))
(unless (find-package "NEW_CODE::WORDCOUNTREQUEST")
  (make-package "NEW_CODE::WORDCOUNTREQUEST"))
(unless (find-package "NEW_CODE::WORDCOUNTRESPONSE")
  (make-package "NEW_CODE::WORDCOUNTRESPONSE"))

(in-package "ROS")





(defclass new_code::WordCountRequest
  :super ros::object
  :slots (_words ))

(defmethod new_code::WordCountRequest
  (:init
   (&key
    ((:words __words) "")
    )
   (send-super :init)
   (setq _words (string __words))
   self)
  (:words
   (&optional __words)
   (if __words (setq _words __words)) _words)
  (:serialization-length
   ()
   (+
    ;; string _words
    4 (length _words)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _words
       (write-long (length _words) s) (princ _words s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _words
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _words (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass new_code::WordCountResponse
  :super ros::object
  :slots (_count ))

(defmethod new_code::WordCountResponse
  (:init
   (&key
    ((:count __count) 0)
    )
   (send-super :init)
   (setq _count (round __count))
   self)
  (:count
   (&optional __count)
   (if __count (setq _count __count)) _count)
  (:serialization-length
   ()
   (+
    ;; uint32 _count
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _count
       (write-long _count s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _count
     (setq _count (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass new_code::WordCount
  :super ros::object
  :slots ())

(setf (get new_code::WordCount :md5sum-) "58903d21a3264f3408d79ba79e9f7c7e")
(setf (get new_code::WordCount :datatype-) "new_code/WordCount")
(setf (get new_code::WordCount :request) new_code::WordCountRequest)
(setf (get new_code::WordCount :response) new_code::WordCountResponse)

(defmethod new_code::WordCountRequest
  (:response () (instance new_code::WordCountResponse :init)))

(setf (get new_code::WordCountRequest :md5sum-) "58903d21a3264f3408d79ba79e9f7c7e")
(setf (get new_code::WordCountRequest :datatype-) "new_code/WordCountRequest")
(setf (get new_code::WordCountRequest :definition-)
      "string words
---
uint32 count

")

(setf (get new_code::WordCountResponse :md5sum-) "58903d21a3264f3408d79ba79e9f7c7e")
(setf (get new_code::WordCountResponse :datatype-) "new_code/WordCountResponse")
(setf (get new_code::WordCountResponse :definition-)
      "string words
---
uint32 count

")



(provide :new_code/WordCount "58903d21a3264f3408d79ba79e9f7c7e")


