class Solution {
    public int singleNumber(int[] nums) {
        final Set<Integer> set = new HashSet<>();

        for (final int num : nums) {
            if (set.contains(num))
                set.remove(num);
            else
                set.add(num);
        }
        return set.iterator().next();
    }
}