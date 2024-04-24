package client;

import java.rmi.Naming;
import remotes.Search;

public class SearchClient {
    public static void main(String[] args) {
        try {
            String searchTrarget = (args.length < 1) ? "p2p" : args[0];
            String url = "rmi://localhost:1099/REMOTE_SEARCH";
            Search remoteSearchObject = (Search) Naming.lookup(url);
            String result = remoteSearchObject.query(searchTrarget);
            System.out.println("Found : " + result);
        } catch (Exception e) {
            System.out.println("Error in Search Client" + e.getMessage());
        }
    }
}
