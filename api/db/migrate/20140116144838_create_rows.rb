class CreateRows < ActiveRecord::Migration
  def change
    create_table :rows do |t|
      t.integer :value
      t.string :label
      t.string :colour

      t.timestamps
    end
  end
end
