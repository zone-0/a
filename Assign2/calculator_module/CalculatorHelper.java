package calculator_module;


/**
* calculator_module/CalculatorHelper.java .
* Generated by the IDL-to-Java compiler (portable), version "3.2"
* from calculator.idl
* Tuesday, April 16, 2024 3:09:12 PM IST
*/

abstract public class CalculatorHelper
{
  private static String  _id = "IDL:calculator_module/Calculator:1.0";

  public static void insert (org.omg.CORBA.Any a, calculator_module.Calculator that)
  {
    org.omg.CORBA.portable.OutputStream out = a.create_output_stream ();
    a.type (type ());
    write (out, that);
    a.read_value (out.create_input_stream (), type ());
  }

  public static calculator_module.Calculator extract (org.omg.CORBA.Any a)
  {
    return read (a.create_input_stream ());
  }

  private static org.omg.CORBA.TypeCode __typeCode = null;
  synchronized public static org.omg.CORBA.TypeCode type ()
  {
    if (__typeCode == null)
    {
      __typeCode = org.omg.CORBA.ORB.init ().create_interface_tc (calculator_module.CalculatorHelper.id (), "Calculator");
    }
    return __typeCode;
  }

  public static String id ()
  {
    return _id;
  }

  public static calculator_module.Calculator read (org.omg.CORBA.portable.InputStream istream)
  {
    return narrow (istream.read_Object (_CalculatorStub.class));
  }

  public static void write (org.omg.CORBA.portable.OutputStream ostream, calculator_module.Calculator value)
  {
    ostream.write_Object ((org.omg.CORBA.Object) value);
  }

  public static calculator_module.Calculator narrow (org.omg.CORBA.Object obj)
  {
    if (obj == null)
      return null;
    else if (obj instanceof calculator_module.Calculator)
      return (calculator_module.Calculator)obj;
    else if (!obj._is_a (id ()))
      throw new org.omg.CORBA.BAD_PARAM ();
    else
    {
      org.omg.CORBA.portable.Delegate delegate = ((org.omg.CORBA.portable.ObjectImpl)obj)._get_delegate ();
      calculator_module._CalculatorStub stub = new calculator_module._CalculatorStub ();
      stub._set_delegate(delegate);
      return stub;
    }
  }

  public static calculator_module.Calculator unchecked_narrow (org.omg.CORBA.Object obj)
  {
    if (obj == null)
      return null;
    else if (obj instanceof calculator_module.Calculator)
      return (calculator_module.Calculator)obj;
    else
    {
      org.omg.CORBA.portable.Delegate delegate = ((org.omg.CORBA.portable.ObjectImpl)obj)._get_delegate ();
      calculator_module._CalculatorStub stub = new calculator_module._CalculatorStub ();
      stub._set_delegate(delegate);
      return stub;
    }
  }

}
