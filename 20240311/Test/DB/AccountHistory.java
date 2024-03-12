package teamProject;

public class AccountHistory {
    private int id;
    private String account_number;
    private String transaction_type;
    private double transaction_amount;
    private double balance;

    public AccountHistory() {
    }

    public AccountHistory(String transaction_type, double transaction_amount, double balance) {
        this.transaction_type = transaction_type;
        this.transaction_amount = transaction_amount;
        this.balance = balance;
    }

    public AccountHistory(int id, String account_number, String transaction_type, double transaction_amount, double balance) {
        this.id = id;
        this.account_number = account_number;
        this.transaction_type = transaction_type;
        this.transaction_amount = transaction_amount;
        this.balance = balance;
    }

    @Override
    public String toString() {
        return "AccountHistoryDTO{" +
                "id=" + id +
                ", account_number='" + account_number + '\'' +
                ", transaction_type='" + transaction_type + '\'' +
                ", transaction_amount=" + transaction_amount +
                ", balance=" + balance +
                '}';
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getAccount_number() {
        return account_number;
    }

    public void setAccount_number(String account_number) {
        this.account_number = account_number;
    }

    public String getTransaction_type() {
        return transaction_type;
    }

    public void setTransaction_type(String transaction_type) {
        this.transaction_type = transaction_type;
    }

    public double getTransaction_amount() {
        return transaction_amount;
    }

    public void setTransaction_amount(double transaction_amount) {
        this.transaction_amount = transaction_amount;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }
}
