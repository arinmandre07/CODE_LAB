package railway;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Main extends javax.swing.JFrame {

    public Main() {
        initComponents();
    }

    private void initComponents() {
        // Create buttons for navigation
        JButton addTrainButton = new JButton("Add Train");
        JButton reservationButton = new JButton("Reservation");
        JButton bookingsButton = new JButton("Bookings");

        // Create a label at the top
        JLabel servicesLabel = new JLabel("Services");
        servicesLabel.setFont(new Font("Arial", Font.BOLD, 20));  // Bold and larger font
        servicesLabel.setForeground(new Color(0, 123, 255));  // Blue color for the label
        servicesLabel.setHorizontalAlignment(SwingConstants.CENTER);

        // Set layout and size
        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Welcome to Railway System");
        setSize(500, 450);  // Increased window size for better UI with label
        setLocationRelativeTo(null);  // Center the window

        // Set background color for the window
        getContentPane().setBackground(new Color(245, 245, 245));  // Light gray background
        setLayout(new GridBagLayout());  // Use GridBagLayout for better layout control

        // Define a GridBagConstraints object for controlling component placement
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.gridx = 0;  // Column
        gbc.gridy = 0;  // Row
        gbc.insets = new Insets(10, 10, 10, 10);  // Add spacing between components

        // Add label at the top
        add(servicesLabel, gbc);
        
        // Increase the button size and customize with modern look
        customizeButton(addTrainButton);
        customizeButton(reservationButton);
        customizeButton(bookingsButton);

        // Add buttons to the frame using GridBagLayout
        gbc.gridy = 1;  // Move to the next row
        gbc.gridwidth = 1;  // One column for the button
        add(addTrainButton, gbc);
        
        gbc.gridy = 2;  // Move to the next row
        add(reservationButton, gbc);
        
        gbc.gridy = 3;  // Move to the next row
        add(bookingsButton, gbc);

        // Action listener for "Add Train" button
        addTrainButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Open the AddTrain page
                addtrain addTrainPage = new addtrain();  // Ensure AddTrain is the correct class name
                addTrainPage.setVisible(true);
                dispose();  // Close the main window
            }
        });

        // Action listener for "Reservation" button
        reservationButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Open the Reservation page
                Reservation reservationPage = new Reservation();  // Ensure correct class name
                reservationPage.setVisible(true);
                dispose();  // Close the main window
            }
        });

        // Action listener for "Bookings" button
        bookingsButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Open the Bookings page
                Bookings bookingsPage = new Bookings();  // Ensure Bookings is the correct class name
                bookingsPage.setVisible(true);
                dispose();  // Close the main window
            }
        });
    }

    // Method to customize button appearance
    private void customizeButton(JButton button) {
        // Set a custom font and larger size
        button.setFont(new Font("Arial", Font.BOLD, 16));  // Larger font

        // Set a rounded border with a color
        button.setBackground(new Color(0, 123, 255));  // Blue color
        button.setForeground(Color.WHITE);  // White text
        button.setFocusPainted(false);
        button.setBorder(BorderFactory.createLineBorder(new Color(0, 123, 255), 2, true));
        button.setOpaque(true);
        button.setPreferredSize(new Dimension(200, 50));  // Larger buttons

        // Add hover effect on button
        button.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseEntered(java.awt.event.MouseEvent evt) {
                button.setBackground(new Color(0, 150, 255));  // Darker blue on hover
            }

            public void mouseExited(java.awt.event.MouseEvent evt) {
                button.setBackground(new Color(0, 123, 255));  // Reset to original blue
            }
        });
    }

    public static void main(String args[]) {
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Main().setVisible(true);
            }
        });
    }
}
