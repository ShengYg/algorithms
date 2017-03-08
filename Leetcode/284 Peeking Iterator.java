public class Solution {
    class PeekingIterator implements Iterator<Integer> {

        private Iterator<Integer> iter;
        private Integer element = null;

        public PeekingIterator(Iterator<Integer> iterator) {
            // initialize any member here.
            iter = iterator;
            if(iter.hasNext())
                element = iter.next();
        }

        // Returns the next element in the iteration without advancing the iterator.
        public Integer peek() {
            return element;
        }

        // hasNext() and next() should behave the same as in the Iterator interface.
        // Override them if needed.
        @Override
        public Integer next() {
            Integer res = element;
            element = iter.hasNext() ? iter.next() : null;
            return res;
        }

        @Override
        public boolean hasNext() {
            return element != null
        }
    }
}
