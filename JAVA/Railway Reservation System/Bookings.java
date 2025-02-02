package railway;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.sql.*;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.JTableHeader;

public class Bookings extends JFrame {
    private static final String URL = "jdbc:mysql://localhost:3306/railwaydb";
    private static final String USER = "root";
    private static final String PASSWORD = "root";
    private JTable table;
    private DefaultTableModel model;

    public Bookings() {
        setTitle("Reservations Booking");
        setSize(1250, 720); 
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLayout(new BorderLayout());

        
        getContentPane().setBackground(Color.WHITE);

        
        model = new DefaultTableModel();
        model.addColumn("ID");
        model.addColumn("IRCTC Username");
        model.addColumn("Train Name");
        model.addColumn("Train Number"); 
        model.addColumn("Departure");
        model.addColumn("Arrival");
        model.addColumn("Journey Date");
        model.addColumn("Tickets");
        model.addColumn("Price");
        model.addColumn("Total");

       
        table = new JTable(model);
        table.setFont(new Font("Segoe UI Semibold", Font.PLAIN, 14)); 
        table.setRowHeight(25);
        table.setGridColor(Color.LIGHT_GRAY);
        table.setBackground(Color.WHITE);

        
        JTableHeader header = table.getTableHeader();
        header.setFont(new Font("Segoe UI Semibold", Font.BOLD, 16));
        header.setBackground(new Color(79, 120, 255));
        header.setForeground(Color.WHITE);

        
        JScrollPane scrollPane = new JScrollPane(table);
        scrollPane.setBackground(Color.WHITE);
        add(scrollPane, BorderLayout.CENTER);

        
        JButton cancelButton = new JButton("Cancel Reservation");
        cancelButton.setFont(new Font("Segoe UI Semibold", Font.BOLD, 14));
        cancelButton.setBackground(new Color(79, 120, 255));
        cancelButton.setForeground(Color.WHITE);
        cancelButton.setFocusPainted(false);
        cancelButton.setBorder(BorderFactory.createEmptyBorder(10, 20, 10, 20));

        cancelButton.addActionListener(this::cancelReservation);
        
        
        JPanel buttonPanel = new JPanel();
        buttonPanel.setBackground(Color.WHITE);
        buttonPanel.add(cancelButton);
        add(buttonPanel, BorderLayout.SOUTH);

        
        loadDataFromDatabase();
        setVisible(true);
    }

    private void loadDataFromDatabase() {
        try (Connection connection = DriverManager.getConnection(URL, USER, PASSWORD);
             Statement stmt = connection.createStatement();
             ResultSet resultSet = stmt.executeQuery("SELECT * FROM reservations")) {

            while (resultSet.next()) {
                model.addRow(new Object[]{
                    resultSet.getInt("id"),
                    resultSet.getString("irctc_username"),
                    resultSet.getString("train_name"),
                    resultSet.getString("train_num"), 
                    resultSet.getString("departure"),
                    resultSet.getString("arrival"),
                    resultSet.getDate("journey_date"),
                    resultSet.getInt("tickets"),
                    resultSet.getInt("price"),
                    resultSet.getInt("total")
                });
            }
        } catch (SQLException e) {
            JOptionPane.showMessageDialog(this, "Error loading data: " + e.getMessage());
        }
    }

    private void cancelReservation(ActionEvent e) {
        int selectedRow = table.getSelectedRow();
        if (selectedRow != -1) {
            int id = (int) model.getValueAt(selectedRow, 0);
            try (Connection connection = DriverManager.getConnection(URL, USER, PASSWORD);
                 PreparedStatement pstmt = connection.prepareStatement("DELETE FROM reservations WHERE id = ?")) {
                pstmt.setInt(1, id);
                pstmt.executeUpdate();
                model.removeRow(selectedRow);
                JOptionPane.showMessageDialog(this, "Reservation Cancelled Successfully!");
            } catch (SQLException ex) {
                JOptionPane.showMessageDialog(this, "Error cancelling reservation: " + ex.getMessage());
            }
        } else {
            JOptionPane.showMessageDialog(this, "Please select a reservation to cancel.");
        }
    }
}
