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
        { title: '订单号', dataIndex: 'no', key: 'no' },
        { title: '时间', dataIndex: 'datetime', key: 'datetime' },
        { title: '金额', dataIndex: 'price', key: 'price' },
        { title: '成本', dataIndex: 'cost', key: 'cost' },
        { title: '利润', dataIndex: 'profit', key: 'profit' },
        { title: '业务员', dataIndex: 'business_manager', key: 'business_manager' },
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
