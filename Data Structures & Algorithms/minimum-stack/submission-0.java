class MinStack {
    private Stack<Integer> newStack; 
    public MinStack() {
        newStack = new Stack<>();
    }
    
    public void push(int val) {
        newStack.push(val);
    }
    
    public void pop() {
        newStack.pop();
    }
    
    public int top() {
        return newStack.peek();
    }
    
    public int getMin() {
        Stack<Integer> tmp = new Stack<>();
        int min = newStack.peek();

        while(!newStack.isEmpty()){
            min = Math.min(min, newStack.peek());
            tmp.push(newStack.pop());
        }

        while(!tmp.isEmpty()){
            newStack.push(tmp.pop());
        }

        return min;
    }
}
