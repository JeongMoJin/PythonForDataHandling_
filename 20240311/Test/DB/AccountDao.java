package teamProject;

import java.sql.*;
import java.util.ArrayList;

public class AccountDao implements IAccountDao {
    private Connection connection = null;

    AccountDao() {
        getConnection();
    }

    public void getConnection() { // 디비 연결 생성자에서 실행
        try {
            String url = "jdbc:mariadb://localhost:3308/team_project";
            String user = "root";
            String password = "5046";

            try {
                Class.forName("org.mariadb.jdbc.Driver");
            } catch (ClassNotFoundException e) {
                e.printStackTrace();
            }

            this.connection = DriverManager.getConnection(url, user, password);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    } // 데이터 베이스 연결

    public boolean insertMember(Member member) {
        String sql = "INSERT INTO team_project.member VALUES (?,?,?,?,?)";
        try (PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
            preparedStatement.setInt(1, member.getId()); // 추가 할 때 자동으로 생성되어서 생략 가능
            preparedStatement.setString(2, member.getMember_id());
            preparedStatement.setString(3, member.getName());
            preparedStatement.setInt(4, member.getAge());
            preparedStatement.setString(5, member.getAddress());

            return preparedStatement.executeUpdate() == 1;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    } // 회원 등록 디비 처리

    public boolean insertAccount(Account account) {
        String sql = "INSERT INTO team_project.account VALUES (?,?,?,?,?,?,?)"; // ? 가 5개라 오류 갯수에 맞게 추가
        try (PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
            preparedStatement.setInt(1, account.getId());  // getId() 도 생략 하면 안됌
            preparedStatement.setString(2, account.getMember_id());
            preparedStatement.setString(3, account.getAccount_type());
            preparedStatement.setString(4, account.getAccount_number());
            preparedStatement.setDouble(5, account.getBalance());
            preparedStatement.setDouble(6, account.getInterest_rate());
            preparedStatement.setDouble(7, account.getFee_rate());

            int result = preparedStatement.executeUpdate(); // executeUpdate() 는 select 제외 성공된 행의수 반환 수행된 행의수를 result에 저장
            if (result > 0) {
                return true;// 성공적으로 반환을 했다면 6이므로 true 가 되고 메서드 종료
            } else {
                System.out.println("계정을 생성하는데 실패했습니다.");
            }
            // return preparedStatement.executeUpdate() == 1;
        } catch (SQLException e) {
            // throw new RuntimeException(e);
            e.printStackTrace();
        }
        return false; // 그게 아니라면 catch 가 실행 되고 false 로 메서드 종료
    } // 계좌 개설 디비 처리

    public void insertAccountHistory(AccountHistory accountHistory) {
        String sql = "INSERT INTO accounthistory (account_number, transaction_type, transaction_amount, balance) VALUES (?, ?, ?, ?)";
        try (PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
            preparedStatement.setString(1, accountHistory.getAccount_number());
            preparedStatement.setString(2, accountHistory.getTransaction_type());
            preparedStatement.setDouble(3, accountHistory.getTransaction_amount());
            preparedStatement.setDouble(4, accountHistory.getBalance());
            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }  // 거래 내역 저장

    public ArrayList<AccountHistory> selectAccountHistories(String account_number) {
        String sql = "SELECT transaction_type, transaction_amount, balance FROM team_project.accounthistory order by id desc ";
        ArrayList<AccountHistory> list = new ArrayList<>();

        try (PreparedStatement preparedStatement = connection.prepareStatement(sql);
             ResultSet resultSet = preparedStatement.executeQuery()) {
            while (resultSet.next()) {
                AccountHistory accountHistory = new AccountHistory(resultSet.getString("transaction_type"),
                        resultSet.getDouble("transaction_amount"), resultSet.getDouble("balance"));
                list.add(accountHistory);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return list;
    } // 특정 계좌 번호에 대한 거래 내역 조회

    public void disConnect() {
        try {
            if (connection != null) {
                connection.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    } // 데이터 베이스 연결 해제

    public Account selectAccount(String account_number) {
        Account account = null;
        String sql = "SELECT * FROM account WHERE account_number= '" + account_number + "'";
//        System.out.println(sql);
        try (PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
            //preparedStatement.setString(1,account_number); insertAccount 처럼 ? 가 있는 것이 아니기 때문에 주석처리
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                if (resultSet.next()) {
                    account = new Account();
                    account.setId(resultSet.getInt("id")); // 자동생성이니 필요없지 않을까
                    account.setMember_id(resultSet.getString("member_id"));
                    account.setAccount_type(resultSet.getString("account_type"));
                    account.setAccount_number(resultSet.getString("account_number"));
                    account.setBalance(resultSet.getDouble("balance"));
                    account.setInterest_rate(resultSet.getDouble("interest_rate"));
                    account.setFee_rate(resultSet.getDouble("fee_rate"));
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
//        System.out.println(account);
        return account;
    } // 특정 계좌 번호의 정보를 가져옴

    public double selectBalance(String account_number) {
        Account account = null;
        double wantBalance = 0;
        String sql = "SELECT balance FROM account WHERE account_number = '" + account_number + "'";
        try (PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
            preparedStatement.setString(1, account_number);
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                if (resultSet.next()) {
                    account = new Account();
                    account.setBalance(resultSet.getDouble("balance"));
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        wantBalance = account.getBalance();
        return wantBalance;
    } // 특정 계좌 번호의 잔액을 가져옴

    @Override
    public void updateBalance(String accountId, double balance) {
    }

    void updateBalance(double amount, String account_number, boolean flag) {
        String sql;
        int cnt = 0;
        sql = String.format("UPDATE account SET balance = ? WHERE (account_number = ?)");

        try (PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
            preparedStatement.setDouble(1, amount); // 1 번 ? 는 잔액(balance)에서 금액(amount)을 빼고 더하는 받아야하고
            preparedStatement.setString(2, account_number); // 2번 ? 가 계좌 번호를 받아야 해서 순서 변경

            cnt = preparedStatement.executeUpdate();
            if (cnt != 1) {
                System.out.println("입출금을 실패하였습니다.");
            } else {
                System.out.println("입출금을 성공하였습니다.");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    } // 특정 계좌 번호의 잔액을 수정

    public int selectAccountIdCnt(String account_number) {
        String sql = "SELECT COUNT(*) AS cnt FROM team_project.account WHERE account_number = ?";
        int cnt;
        try (PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
            preparedStatement.setString(1, account_number);
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                resultSet.next();
                cnt = resultSet.getInt(1);
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return cnt;
    } // 해당 계좌번호의 계좌 개수를 반환

    public int selectMemberIdCnt(String member_id) {
        String sql = "SELECT COUNT(*) AS cnt FROM team_project.member WHERE member_id = ?";
        int cnt;
        try (PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
            preparedStatement.setString(1, member_id);
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                resultSet.next();
                cnt = resultSet.getInt(1);
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return cnt;
    } // 해당 아이디의 회원 개수를 반환

    //    @Override
//    public boolean selectPartCnt(Account account) {
//        return false;
//    }
    public boolean selectPartCntOne(Account account) {
        String account_type = account.getAccount_type();
        String sql = "SELECT count(account_type) FROM account WHERE account_type = '" + account_type + "'  IN ('1')"; // 물음표가 없어도 됌
        int cnt;
        try (PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
            preparedStatement.setString(1, account_type); // ? 가 없어도 되므로 주석 처리
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                resultSet.next();
                cnt = resultSet.getInt(1);
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        if (cnt == 1) {
            return true;
        } else {
            return false;
        }
    }

    public boolean selectPartCntTwo(Account account) {
        String account_type = account.getAccount_type();
        String sql = "SELECT count(account_type) FROM account WHERE account_type = '" + account_type + "' IN ('2')";
        int cnt;
        try (PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
            preparedStatement.setString(1, account_type);
            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                resultSet.next();
                cnt = resultSet.getInt(1);
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        if (cnt == 1) {
            return true;
        } else {
            return false;
        }
    }
}




