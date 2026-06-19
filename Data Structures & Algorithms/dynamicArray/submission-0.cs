public class DynamicArray {
    
    private int _capacity;
    private _arr = int[];
    private endOfArr = 0;

    public DynamicArray(int capacity) {
        _capacity = capacity;
        _arr = new int[_capacity]
    }

    public int Get(int i) {
        return _arr[i];
    }

    public void Set(int i, int n) {
        _arr[i] = n;
    }

    public void PushBack(int n) {
        if (endOfArr < _capacity)
        {
            _arr[endOfArr] = n;
        }
        else
        {
            Resize();
            _arr[endOfArr] = n;
        }
        endOfArr++;
    }

    public int PopBack() {
        if (endOfArr > 0)
        {
            endOfArr--;
            return _arr[endOfArr];
        }
        else
        {
            throw new Exception("Array is empty");
        }
    }

    private void Resize() {
        _capacity *= 2;
    }

    public int GetSize() {
        return endOfArr;
    }

    public int GetCapacity() {
        return _capacity;
    }
}
