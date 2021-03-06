package teste.rest.Service;

import teste.rest.model.AccountModel;
import teste.rest.model.AuthenticationModel;
import teste.rest.model.TransactionModel;

import java.util.List;
import java.util.Map;

/**
 * Interface from Account methods
 * Created by allan on 02-06-2017.
 */
public interface AccountService {

    public AuthenticationModel createAccount(AccountModel input, Map<String, AccountModel> accounts);
    public double getBalance(String token, Map<String, AccountModel> accounts);
    public boolean deposit(TransactionModel input, Map<String, AccountModel> accounts);
    public boolean  withdraw(TransactionModel input, Map<String, AccountModel> accounts);
    public boolean  transferSameBank(TransactionModel input, Map<String, AccountModel> accounts);
    public boolean transferBetwenbBanks(TransactionModel input, Map<String, AccountModel> accounts);
    public List<AccountModel> listAll(Map<String, AccountModel> account);
    public String verify(Map<String, AccountModel> account,AccountModel input);
}
