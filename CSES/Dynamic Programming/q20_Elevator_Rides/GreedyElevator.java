import java.util.*;

public class GreedyElevator {
    public static int greedyElevatorRides(List<Integer> weights, int maxWt) {
        Collections.sort(weights, Collections.reverseOrder());
        int rides = 0;
        
        while (!weights.isEmpty()) {
            int cap = maxWt;
            int i = 0;
            while (i < weights.size()) {
                if (weights.get(i) <= cap) {
                    cap -= weights.get(i);
                    weights.remove(i);
                } else {
                    i++;
                }
            }
            rides++;
        }
        return rides;
    }
    
    public static void main(String[] args) {
        int n = 4, x = 10;
        List<Integer> weights = new ArrayList<>(Arrays.asList(4, 8, 6, 1));
        System.out.println(greedyElevatorRides(weights, x)); 
    }
}
