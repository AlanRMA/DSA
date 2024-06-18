public class LinearSearchExample {
    public static void main(String[] args) {
        int[] array = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
        int key = 40;
        
        int index = linearSearch(array, key);
        if (index != -1) {
            System.out.println("Elemento " + key + " encontrado na posição: " + index);
        } else {
            System.out.println("Elemento " + key + " não encontrado no array.");
        }
    }

    public static int linearSearch(int[] array, int key) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == key) {
                return i;
            }
        }
        return -1;
    }
}
