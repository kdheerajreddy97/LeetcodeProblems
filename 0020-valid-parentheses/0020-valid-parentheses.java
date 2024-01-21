class Solution {
    public boolean isValid(String s) {
        Stack<Character> mystack = new Stack();
        
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            if (c == '(' || c == '{' || c == '['){
                mystack.push(c);
            }
            else {
                if (mystack.isEmpty())
                    {
                        return false;
                    }
                char top = mystack.pop();
                if ( (c==')' && top != '(')||
                     (c==']' && top != '[')||
                     (c=='}' && top != '{')){
                    return false;
                }
            }
        }
            return mystack.isEmpty();
    }
}