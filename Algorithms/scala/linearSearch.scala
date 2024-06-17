object Script{
    def RecLinearSearch(li: List[Int], target : Int):Boolean  = {
        def helper(n:Int):Boolean = {
            if (li(n) == target) true
            else if (n == 0) false
            else helper(n-1)
    }
        helper(li.length-1)
    }
    def main(args: Array[String]): Unit = {
        val li = List(1,2,3,4,5)
        val target = 3
        val result = RecLinearSearch(li, target)
        println(result)
    }
}