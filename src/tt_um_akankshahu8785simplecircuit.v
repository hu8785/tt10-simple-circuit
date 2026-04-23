`default_nettype none
module tt_um_akankshahu8785simplecircuit (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

    wire A = ui_in[0];
    wire B = ui_in[1];
    wire C = ui_in[2];

    wire AB;
    wire C_not;
    wire F;

    // Logic implementation: F = AB + C'
    and g1(AB, A, B);
    not g2(C_not, C);
    or  g3(F, AB, C_not);

    // Assign outputs
    assign uo_out[0] = F;
    assign uo_out[1] = 1'b0;
    assign uo_out[2] = 1'b0;
    assign uo_out[3] = 1'b0;
    assign uo_out[4] = 1'b0;
    assign uo_out[5] = 1'b0;
    assign uo_out[6] = 1'b0;
    assign uo_out[7] = 1'b0;

    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // Prevent unused input warnings
    wire _unused = &{ena, clk, rst_n, ui_in[7:3], uio_in, 1'b0};

endmodule
