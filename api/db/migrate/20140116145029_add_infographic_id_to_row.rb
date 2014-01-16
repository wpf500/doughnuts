class AddInfographicIdToRow < ActiveRecord::Migration
  def change
    add_column :rows, :infographic_id, :integer
  end
end
