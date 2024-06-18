object Script{
    def RecBinarySearch(li: List[Int], target : Int):Boolean  = {
        def helper(l: Int, r: Int): Boolean = {
            if (l > r) false
            val mid = (l + r) / 2
            if (li(mid) == target) true
            else if (li(mid) < target) helper(mid + 1, r)
            else helper(l, mid - 1)
    }
        return helper(0,li.length -1)
    }
    def main(args: Array[String]): Unit = {
        val li = List(1,2,3,4,5)
        val target = 7
        val result = RecBinarySearch(li, target)
        println(result)
    }
}