import java.util.Arrays;

public class bubbleSortExample {
    public static void main(String[] args) {
        int[] array = {1, 3, 5, 2, 10, 9, 8, 6, 7, 4};
        int[] sort = bubbleSort(array);
        
        System.out.println("Array original:");
        System.out.println(Arrays.toString(array));

        System.out.println("Array ordenado:");
        System.out.println(Arrays.toString(sort));
        
    }
    public static int[] bubbleSort(int[] array){
        int[] sort = Arrays.copyOf(array, array.length);
        boolean swapped;
        int n = sort.length;

        for (int i = 0 ; i < n-1 ; i++){
            swapped = false;
            for ( int j = 0 ; j < n - 1 - i; j++){
                if (sort[j] > sort[j + 1]){
                    // troca
                    int temp = sort[j];
                    sort[j] = sort[j + 1];
                    sort[j + 1] = temp;
                    swapped = true;
                }
            }
            if(!swapped){
                break;
            }
        }
        return sort;
    }
}
