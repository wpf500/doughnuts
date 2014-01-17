class AddChartTypeToLineChart < ActiveRecord::Migration
  def change
    add_column :line_charts, :chart_type, :string
  end
end
