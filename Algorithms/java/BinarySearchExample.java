public class BinarySearchExample {
    public static void main(String[] args) {
        int[] array = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
        int key = 40;
        
        int index = binarySearch(array, key);
        if (index != -1) {
            System.out.println("Elemento " + key + " encontrado na posição: " + index);
        } else {
            System.out.println("Elemento " + key + " não encontrado no array.");
        }
    }
    public static int binarySearch(int[] array, int key){
        int min = 0;
        int max = array.length -1;
        while (min <= max){
            int mid = min + (max - min) / 2;
            if ( array[mid] == key){
                return mid;
            }
            else if (array[mid] < key) {
                min = mid + 1;
            }
            else{
                max = mid -1;
            }
        }
        return -1;
    }
}
