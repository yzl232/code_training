# encoding=utf-8
#How does a site like Facebook store "Likes" ?

#简单的用hashtable(set )吧。。
# 每个post   有一个hashtable  .   val   (set).   存了user id.
# key  post ID  val:  user ID