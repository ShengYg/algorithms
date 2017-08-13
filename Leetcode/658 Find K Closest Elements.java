import java.util.stream.*;
class Pair<L, R>{
    L left;
    R right;
    Pair(L left, R right){
        this.left = left;
        this.right = right;
    }
}

public class Solution {
    public List<Integer> findClosestElements(List<Integer> arr, int k, int x) {
        ArrayList<Pair<Integer, Integer>> res = new ArrayList<>();
        for(int item: arr)
            res.add(new Pair<>(Math.abs(item - x), item));
        Collections.sort(res, (a, b) -> {
            if(a.left == b.left)
                return a.right - b.right;
            else
                return a.left - b.left;
        });
        List<Integer> ret = res.subList(0, k).stream().map(a -> a.right).collect(Collectors.toList());
        Collections.sort(ret);
        return ret;
    }
}
