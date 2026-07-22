class Node {
private:
    int value;
    Node *next;
    friend class LinkedList;
    Node(int value = 0, Node *next = nullptr): value{value}, next{next} {}
};

class LinkedList {
private:
    Node *head;
    Node *tail;
public:
    LinkedList(): head{nullptr}, tail{nullptr} {}

    ~LinkedList() {
        Node *current = head;
        while (current) {
            Node *tmp = current;
            current = current->next;
            delete tmp;
        }
    }

    int get(int index) {
        int i = 0;
        Node *current = head;
        while (current) {
            if (i == index) {
                return current->value;
            }
            current = current->next;
            i++;
        }
        return -1;
    }

    void insertHead(int val) {
        Node *n = new Node(val, head);
        head = n;
        if (!tail) tail = n;
    }
    
    void insertTail(int val) {
        Node *n = new Node(val);
        if (!tail) {
            head = tail = n;
        } else {
            tail->next = n;
            tail = n;
        }
    }

    bool remove(int index) {
        if (index < 0 || !head) return false;

        if (index == 0) {
            Node *tmp = head;
            head = head->next;
            if (!head)
                tail = nullptr;
            delete tmp;
            return true;
        }

        Node *prev = head;
        int i = 0;
        while (prev->next && i + 1 < index) {
            prev = prev->next;
            ++i;
        }

        if (prev->next) {
            Node *toDel = prev->next;
            prev->next = toDel->next;
            if (toDel == tail)
                tail = prev;
            delete toDel;
            return true;
        }

        return false;
    }

    vector<int> getValues() {
        vector<int> values;
        Node *current = head;

        while (current) {
            values.push_back(current->value);
            current = current->next;
        }
        return std::move(values);
    }
};
