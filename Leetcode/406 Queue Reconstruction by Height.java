public class Solution {
    public int[][] reconstructQueue(int[][] people) {
        if (people == null || people.length == 0 || people[0].length == 0)
            return new int[0][0];
        Arrays.sort(people, (int[] a, int[] b) -> {
            if (b[0] == a[0]) return a[1] - b[1];
                return b[0] - a[0];
        });

        int n = people.length;
        List<int[]> tmp = new ArrayList<>();
        for (int[] p: people)
            tmp.add(p[1], p);

        return tmp.toArray(new int[people.length][]);
    }
}
