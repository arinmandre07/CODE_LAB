package railway;

import java.sql.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import com.toedter.calendar.JDateChooser;
import java.util.Date;

public class Reservation extends javax.swing.JFrame {
    private JTextField tfUsername, tfTickets, tfPrice, tfTotal, tfTrainNumber;
    private JComboBox<String> cbTrainName, cbDeparture, cbArrival;
    private JDateChooser dateChooser;
    private JButton btnSubmit;

    public Reservation() {
        // Frame initialization
        setTitle("Railway Reservation System");
        setSize(400, 500);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        
        JPanel panel = new JPanel();
        panel.setLayout(null);
        panel.setBackground(new Color(255, 255, 255)); // Light blue background
        add(panel);
        
        Font font = new Font("Segoe UI Semibold", Font.BOLD, 14);
        Font font1 = new Font("Segoe UI Semibold", Font.PLAIN, 12);

        JLabel lblUsername = new JLabel("IRCTC Username:");
        lblUsername.setBounds(10, 20, 120, 25);
        lblUsername.setFont(font);
        panel.add(lblUsername);

        tfUsername = new JTextField();
        tfUsername.setBounds(140, 20, 200, 25);
        tfUsername.setFont(font1);
        panel.add(tfUsername);

        JLabel lblTrainName = new JLabel("Train Name:");
        lblTrainName.setBounds(10, 50, 120, 25);
        lblTrainName.setFont(font);
        panel.add(lblTrainName);

        cbTrainName = new JComboBox<>();
        cbTrainName.setBounds(140, 50, 200, 25);
        cbTrainName.setFont(font1);
        panel.add(cbTrainName);

        JLabel lblTrainNumber = new JLabel("Train Number:");
        lblTrainNumber.setBounds(10, 80, 120, 25);
        lblTrainNumber.setFont (font);
        panel.add(lblTrainNumber);

        tfTrainNumber = new JTextField();
        tfTrainNumber.setBounds(140, 80, 200, 25);
        tfTrainNumber.setFont(font1);
        tfTrainNumber.setEditable(false);
        panel.add(tfTrainNumber);

        JLabel lblDeparture = new JLabel("Departure:");
        lblDeparture.setBounds(10, 110, 120, 25);
        lblDeparture.setFont(font);
        panel.add(lblDeparture);

        cbDeparture = new JComboBox<>();
        cbDeparture.setBounds(140, 110, 200, 25);
        cbDeparture.setFont(font1);
        panel.add(cbDeparture);

        JLabel lblArrival = new JLabel("Arrival:");
        lblArrival.setBounds(10, 140, 120, 25);
        lblArrival.setFont(font);
        panel.add(lblArrival);

        cbArrival = new JComboBox<>();
        cbArrival.setBounds(140, 140, 200, 25);
        cbArrival.setFont(font1);
        panel.add(cbArrival);

        JLabel lblJourneyDate = new JLabel("Journey Date:");
        lblJourneyDate.setBounds(10, 170, 120, 25);
        lblJourneyDate.setFont(font);
        panel.add(lblJourneyDate);

        dateChooser = new JDateChooser();
        dateChooser.setBounds(140, 170, 200, 25);
        dateChooser.setFont(font1);
        dateChooser.setDateFormatString("yyyy-MM-dd");
        panel.add(dateChooser);

        JLabel lblTickets = new JLabel("Tickets:");
        lblTickets.setBounds(10, 200, 120, 25);
        lblTickets.setFont(font);
        panel.add(lblTickets);

        tfTickets = new JTextField();
        tfTickets.setBounds(140, 200, 200, 25);
        tfTickets.setFont(font1);
        panel.add(tfTickets);

        JLabel lblPrice = new JLabel("Price per Ticket:");
        lblPrice.setBounds(10, 230, 120, 25);
        lblPrice.setFont(font);
        panel.add(lblPrice);

        tfPrice = new JTextField();
        tfPrice.setBounds(140, 230, 200, 25);
        tfPrice.setFont(font1);
        tfPrice.setEditable(false);
        panel.add(tfPrice);

        JLabel lblTotal = new JLabel("Total Price:");
        lblTotal.setBounds(10, 260, 120, 25);
        lblTotal.setFont(font);
        panel.add(lblTotal);

        tfTotal = new JTextField();
        tfTotal.setBounds(140, 260, 200, 25);
        tfTotal.setFont(font1);
        tfTotal.setEditable(false);
        panel.add(tfTotal);

        btnSubmit = new JButton("Submit");
        btnSubmit.setBounds(140, 300, 100, 30);
        btnSubmit.setFont(font);
        btnSubmit.setBackground(new Color(79, 120, 255)); // Steel blue button
        btnSubmit.setForeground(Color.WHITE);
        panel.add(btnSubmit);

        btnSubmit.addActionListener(e -> insertReservation());
        cbTrainName.addActionListener(e -> fetchTrainDetails());
        tfTickets.addActionListener(e -> calculateTotal());

        loadTrainData();
        setVisible(true);
    }

    private void loadTrainData() {
    String query = "SELECT DISTINCT train_name FROM train";  // Only fetch unique train names
    try (Connection conn = getConnection(); Statement stmt = conn.createStatement(); ResultSet rs = stmt.executeQuery(query)) {
        
        // Clear any existing items to avoid duplicates if this method is called again
        cbTrainName.removeAllItems();
        
        while (rs.next()) {
            String trainName = rs.getString("train_name");
            cbTrainName.addItem(trainName);  // Add unique train names to the combo box
        }
    } catch (Exception ex) {
        JOptionPane.showMessageDialog(null, "Error: " + ex.getMessage());
    }
}



    private void fetchTrainDetails() {
    String query = "SELECT train_no, start_station, destination, price FROM train WHERE train_name = ?";
    try (Connection conn = getConnection(); PreparedStatement pst = conn.prepareStatement(query)) {
        pst.setString(1, (String) cbTrainName.getSelectedItem());
        ResultSet rs = pst.executeQuery();
        
        // Clear existing items to avoid duplicates
        cbDeparture.removeAllItems();
        cbArrival.removeAllItems();
        
        if (rs.next()) {
            // Set the train number and price
            tfTrainNumber.setText(rs.getString("train_no"));
            tfPrice.setText(String.valueOf(rs.getDouble("price")));

            // Add departure and arrival stations
            do {
                cbDeparture.addItem(rs.getString("start_station"));
                cbArrival.addItem(rs.getString("destination"));
            } while (rs.next()); // Continue for all records that match the selected train name
        }
    } catch (Exception ex) {
        JOptionPane.showMessageDialog(null, "Error: " + ex.getMessage());
    }
}



    private void calculateTotal() {
        try {
            int tickets = Integer.parseInt(tfTickets.getText());
            double price = Double.parseDouble(tfPrice.getText());
            tfTotal.setText(String.valueOf(tickets * price));
        } catch (NumberFormatException e) {
            tfTotal.setText("");
        }
    }

    private void insertReservation() {
    String query = "INSERT INTO reservations (irctc_username, train_name, train_num, departure, arrival, journey_date, tickets, price, total) " +
                   "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)";
    try (Connection conn = getConnection(); PreparedStatement pst = conn.prepareStatement(query)) {
        pst.setString(1, tfUsername.getText());
        pst.setString(2, (String) cbTrainName.getSelectedItem());
        pst.setString(3, tfTrainNumber.getText());  // Using correct column name 'train_num'
        pst.setString(4, (String) cbDeparture.getSelectedItem());
        pst.setString(5, (String) cbArrival.getSelectedItem());

        Date selectedDate = dateChooser.getDate();
        if (selectedDate != null) {
            pst.setDate(6, new java.sql.Date(selectedDate.getTime()));
        } else {
            JOptionPane.showMessageDialog(null, "Please select a valid date.");
            return;
        }

        pst.setInt(7, Integer.parseInt(tfTickets.getText()));
        pst.setDouble(8, Double.parseDouble(tfPrice.getText()));
        pst.setDouble(9, Double.parseDouble(tfTotal.getText()));

        pst.executeUpdate();
        JOptionPane.showMessageDialog(null, "Your Journey Has Been Reserved Successfully!");
    } catch (Exception ex) {
        JOptionPane.showMessageDialog(null, "Error: " + ex.getMessage());
    }
}


    private Connection getConnection() throws SQLException {
        return DriverManager.getConnection("jdbc:mysql://localhost:3306/railwaydb", "root", "root");
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(Reservation::new);
    }
}
