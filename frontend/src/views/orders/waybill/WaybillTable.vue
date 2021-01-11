<template>
  <a-table :columns="columns" :data-source="tableData">
    <a slot="action" slot-scope="" href="javascript:;">详情</a>
    <p slot="expandedRowRender" slot-scope="record" style="margin: 0">
      {{ record.description }}
    </p>
  </a-table>
</template>
<script>

export default {
  props: {
    columns: {
      type: Array,
      required: true,
      default: function () {
                return [
        { title: '订单号', dataIndex: 'name', key: 'name' },
        { title: '销售编号', dataIndex: 'age', key: 'age' },
        { title: '金额', dataIndex: 'address', key: 'address' },
        { title: '成本', dataIndex: 'chenben', key: 'x' },
        { title: '利润', dataIndex: 'lirun', key: 'y' },
        { title: '采购单', dataIndex: 'caigoudan', key: 'z' },
        { title: '操作', dataIndex: 'action1', key: 'w', scopedSlots: { customRender: 'action' } }
      ]
            }
    },
    tableData: {
      type: Array,
      required: false,
      default: function () {
        return []
      }
    }
  },
  data () {
    return {

      // data,
      // columns
    }
  }
}
</script>
