package remotes;

import java.rmi.*;
import java.rmi.server.*;

public class SearchQuery extends UnicastRemoteObject implements Search {
    public SearchQuery() throws RemoteException {
        super();
    }

    public String query(String search) throws RemoteException {
        if (search.equals("p2p")) {
            return "Found 1 Result";
        }
        return "No result found";
    }
}
