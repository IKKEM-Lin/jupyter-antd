import { useModelState } from "@anywidget/react";
import {
  Form,
  FormItem,
  DatePicker,
  Checkbox,
  Cascader,
  Editable,
  Input,
  NumberPicker,
  Switch,
  Password,
  PreviewText,
  Radio,
  Reset,
  Select,
  Space,
  Submit,
  TimePicker,
  Transfer,
  TreeSelect,
  Upload,
  FormGrid,
  FormLayout,
  FormTab,
  FormCollapse,
  ArrayTable,
  ArrayCards,
  FormButtonGroup,
} from "@formily/antd-v5";
import { createForm } from "@formily/core";
import { createSchemaField, ISchema } from "@formily/react";
import { Card, Slider, Rate, Modal, Button, Divider } from "antd";
import React, { useEffect, useState } from "react";
import FileSelectorForFormily from "./_FileSelectorForFormily";

import type {ISubmitProps} from "@formily/antd-v5";
import type {ButtonProps} from "antd/lib/button";

const Text: React.FC<{
  value?: string;
  content?: string;
  mode?: "normal" | "h1" | "h2" | "h3" | "p";
}> = ({ value, mode, content, ...props }) => {
  const tagName = mode === "normal" || !mode ? "div" : mode;
  return React.createElement(tagName, props, value || content);
};

const SchemaField = createSchemaField({
  components: {
    Space,
    FormGrid,
    FormLayout,
    FormTab,
    FormCollapse,
    ArrayTable,
    ArrayCards,
    FormItem,
    DatePicker,
    Checkbox,
    Cascader,
    Editable,
    Input,
    Text,
    NumberPicker,
    Switch,
    Password,
    PreviewText,
    Radio,
    Reset,
    Select,
    Submit,
    TimePicker,
    Transfer,
    TreeSelect,
    Upload,
    Card,
    Slider,
    Rate,
    FileSelectorForFormily,  // Custom component
  },
});

const form = createForm();

interface IOptions {
  show_modal: boolean;
  ok_label: string;
  cancel_label: string;
  ok_props: ISubmitProps;
  cancel_props: ButtonProps;
}

const Formily: React.FC = () => {
  const [schema] = useModelState<ISchema>("schema");
  const [value, setValue] = useModelState<Record<string, any>>("value");
  const [options] = useModelState<IOptions>("options");
  const [isModalOpen, setIsModalOpen] = useState(true);

  const {show_modal, ok_label, cancel_label, ok_props, cancel_props} = options;

  const handleOK = (data: Record<string, any>) => {
    setValue(data);
    setIsModalOpen(false);
  };

  const handleCancel = () => {
    setIsModalOpen(false);
  };

  useEffect(() => {
    console.log(value);
  }, [value]);

  const formResult = (
    <Form form={form} layout="vertical">
      <SchemaField schema={schema} />
      <Divider />
      <FormButtonGroup>
        <Submit {...ok_props} onSubmit={handleOK}>{ok_label}</Submit>
        {show_modal && <Button {...cancel_props} onClick={handleCancel}>{cancel_label}</Button>}
      </FormButtonGroup>
    </Form>
  );

  if (!show_modal) {
    return formResult;
  }

  return (
    <Modal
      title=""
      open={isModalOpen}
      footer={null}
      onCancel={handleCancel}
    >
      <div onKeyDown={(evt) => evt.stopPropagation()}>{formResult}</div>
    </Modal>
  );
};

export default Formily;
