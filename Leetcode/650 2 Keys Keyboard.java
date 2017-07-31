public class Solution {
    public int minSteps(int n) {
        if(n <= 1)
            return 0;
        ArrayList<Integer> res = new ArrayList<>();
        devide(res, n, 2);
        int sum = 0;
        for(int i: res)
            sum += i;
        return sum;
    }

    public void devide(List<Integer> res,int num, int start){
        int temp = num;
        boolean flag = false;
        for(int i = start; i <= Math.sqrt(num); i++){
            if(num % i == 0){
                res.add(i);
                temp = num / i;
                start = i;
                flag = true;
                break;
            }
        }
        if(flag)
            devide(res, temp, start);
        else
            res.add(temp);
    }
}
