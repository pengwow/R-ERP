<template>
  <div id="components-form-demo-advanced-search">
    <a-form class="ant-advanced-search-form" :form="form" @submit="handleSearch">
      <a-row :gutter="24">
        <a-col
          v-for="i in searchItem"
          :key="i.id"
          :span="8"
          :style="{ display: i.display }"
        >
          <a-form-item :label="`${i.name}`">
            <a-input
              v-decorator="[
                `${i.name}`,
                {
                  rules: [
                    {
                      required: i.required,
                      message: 'Input something!',
                    },
                  ],
                },
              ]"
              placeholder="placeholder"
            />
          </a-form-item>
        </a-col>
      </a-row>
      <a-row>
        <a-col :span="24" :style="{ textAlign: 'right' }">
          <a-button type="primary" html-type="submit">
            Search
          </a-button>
          <a-button :style="{ marginLeft: '8px' }" @click="handleReset">
            Clear
          </a-button>
          <a :style="{ marginLeft: '8px', fontSize: '12px' }" @click="toggle">
            Collapse <a-icon :type="expand ? 'up' : 'down'" />
          </a>
        </a-col>
      </a-row>
    </a-form>
  </div>
</template>
<script>
import { getOrderList } from '@/api/order'
export default {
  data () {
    return {
      expand: false,
      form: this.$form.createForm(this, { name: 'advanced_search' }),
      searchItem: [
        { 'id': 'PK', 'name': '订单单号', 'display': 'block', 'required': false },
        { 'id': 'PK3', 'name': '采购单号', 'display': 'block', 'required': false },
        { 'id': 'PK1', 'name': '转运单号', 'display': 'block', 'required': false },
        { 'id': 'PK1', 'name': '货品型号', 'display': 'block', 'required': false },
        { 'id': 'PK1', 'name': '货品颜色', 'display': 'block', 'required': false },
        { 'id': 'PK2', 'name': '货单号', 'display': 'none', 'required': false }
      ]
    }
  },
  computed: {
    count () {
      return this.expand ? 11 : 7
    }
  },
  updated () {
    console.log('updated')
  },
  methods: {
    handleSearch (e) {
      e.preventDefault()
      this.form.validateFields((error, values) => {
        console.log('error', error)
        console.log('Received values of form: ', values)
      })
      getOrderList()
    },

    handleReset () {
      this.form.resetFields()
    },

    toggle () {
      this.expand = !this.expand
    }
  }
}
</script>
<style>
.ant-advanced-search-form {
  padding: 24px;
  background: #fbfbfb;
  border: 1px solid #d9d9d9;
  border-radius: 6px;
}

.ant-advanced-search-form .ant-form-item {
  display: flex;
}

.ant-advanced-search-form .ant-form-item-control-wrapper {
  flex: 1;
}

#components-form-demo-advanced-search .ant-form {
  max-width: none;
}
#components-form-demo-advanced-search .search-result-list {
  margin-top: 16px;
  border: 1px dashed #e9e9e9;
  border-radius: 6px;
  background-color: #fafafa;
  min-height: 200px;
  text-align: center;
  padding-top: 80px;
}
</style>
