class DynamicArray {
private:
    int *arr;
    int capacity;
    int size;
public:

    DynamicArray(int capacity) {
        this->size = 0;
        this->capacity = capacity;
        arr = new int[capacity];
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (size == capacity) {
            resize();
        }
        arr[size++] = n;
    }

    int popback() {
        return arr[--size];
    }

    void resize() {
        capacity *= 2;
        int *newArr = new int[capacity];

        for (int i = 0; i < size; i++) {
            newArr[i] = arr[i];
        }
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return capacity;
    }
};
