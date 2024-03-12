package teamProject;


import java.util.Scanner;

public class AccountView {
    public static void printMenu() {
        System.out.println("===========MENU===========");
        System.out.println("1. 회원 등록");
        System.out.println("2. 계좌 개설");
        System.out.println("3. 입금");
        System.out.println("4. 출금");
        System.out.println("5. 잔액 및 거래 내역 조회");
        System.out.println("6. 프로그램종료");
        System.out.println();
    }

    public static void main(String[] args) {
        AccountManager accountManager = new AccountManager();
        Scanner stdIn = new Scanner(System.in);

        while (true) {
            printMenu();
            System.out.print("선택: ");
            int choice = stdIn.nextInt();
            switch (choice) {
                case 1:
                    accountManager.addMember();
                    break;
                case 2:
                    accountManager.addAccount();
                    break;
                case 3:
                    accountManager.deposit();
                    break;
                case 4:
                    accountManager.withdraw();
                    break;
                case 5:
                    accountManager.viewHistory();
                    break;
                case 6:
                    accountManager.disConnect();
                    System.out.println("종료합니다.");
                    stdIn.close();
                    return;
                default:
                    System.out.println("잘못누르셨습니다.\n다시선택해주세요.");
                    break;
            }
        }
    }
}

