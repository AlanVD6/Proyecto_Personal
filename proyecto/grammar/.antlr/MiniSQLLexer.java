// Generated from d:/Automatas_Practicas/proyecto_personal/proyecto/grammar/miniSQL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class miniSQLLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SELECT=1, FROM=2, WHERE=3, AND=4, OR=5, STAR=6, COMMA=7, EQ=8, NEQ=9, 
		LT=10, GT=11, LEQ=12, GEQ=13, INT=14, STRING=15, ID=16, WS=17;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"SELECT", "FROM", "WHERE", "AND", "OR", "STAR", "COMMA", "EQ", "NEQ", 
			"LT", "GT", "LEQ", "GEQ", "INT", "STRING", "ID", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, "'*'", "','", "'='", "'!='", "'<'", 
			"'>'", "'<='", "'>='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SELECT", "FROM", "WHERE", "AND", "OR", "STAR", "COMMA", "EQ", 
			"NEQ", "LT", "GT", "LEQ", "GEQ", "INT", "STRING", "ID", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public miniSQLLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "miniSQL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0011k\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b"+
		"\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\f\u0001\f\u0001\f\u0001\r\u0004\rQ\b\r\u000b\r\f\rR\u0001"+
		"\u000e\u0001\u000e\u0005\u000eW\b\u000e\n\u000e\f\u000eZ\t\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0005\u000f`\b\u000f\n\u000f"+
		"\f\u000fc\t\u000f\u0001\u0010\u0004\u0010f\b\u0010\u000b\u0010\f\u0010"+
		"g\u0001\u0010\u0001\u0010\u0000\u0000\u0011\u0001\u0001\u0003\u0002\u0005"+
		"\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n"+
		"\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011"+
		"\u0001\u0000\u0013\u0002\u0000SSss\u0002\u0000EEee\u0002\u0000LLll\u0002"+
		"\u0000CCcc\u0002\u0000TTtt\u0002\u0000FFff\u0002\u0000RRrr\u0002\u0000"+
		"OOoo\u0002\u0000MMmm\u0002\u0000WWww\u0002\u0000HHhh\u0002\u0000AAaa\u0002"+
		"\u0000NNnn\u0002\u0000DDdd\u0001\u000009\u0001\u0000\'\'\u0003\u0000A"+
		"Z__az\u0004\u000009AZ__az\u0003\u0000\t\n\r\r  n\u0000\u0001\u0001\u0000"+
		"\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000"+
		"\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000"+
		"\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000"+
		"\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000"+
		"\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000"+
		"\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000"+
		"\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000"+
		"\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0001"+
		"#\u0001\u0000\u0000\u0000\u0003*\u0001\u0000\u0000\u0000\u0005/\u0001"+
		"\u0000\u0000\u0000\u00075\u0001\u0000\u0000\u0000\t9\u0001\u0000\u0000"+
		"\u0000\u000b<\u0001\u0000\u0000\u0000\r>\u0001\u0000\u0000\u0000\u000f"+
		"@\u0001\u0000\u0000\u0000\u0011B\u0001\u0000\u0000\u0000\u0013E\u0001"+
		"\u0000\u0000\u0000\u0015G\u0001\u0000\u0000\u0000\u0017I\u0001\u0000\u0000"+
		"\u0000\u0019L\u0001\u0000\u0000\u0000\u001bP\u0001\u0000\u0000\u0000\u001d"+
		"T\u0001\u0000\u0000\u0000\u001f]\u0001\u0000\u0000\u0000!e\u0001\u0000"+
		"\u0000\u0000#$\u0007\u0000\u0000\u0000$%\u0007\u0001\u0000\u0000%&\u0007"+
		"\u0002\u0000\u0000&\'\u0007\u0001\u0000\u0000\'(\u0007\u0003\u0000\u0000"+
		"()\u0007\u0004\u0000\u0000)\u0002\u0001\u0000\u0000\u0000*+\u0007\u0005"+
		"\u0000\u0000+,\u0007\u0006\u0000\u0000,-\u0007\u0007\u0000\u0000-.\u0007"+
		"\b\u0000\u0000.\u0004\u0001\u0000\u0000\u0000/0\u0007\t\u0000\u000001"+
		"\u0007\n\u0000\u000012\u0007\u0001\u0000\u000023\u0007\u0006\u0000\u0000"+
		"34\u0007\u0001\u0000\u00004\u0006\u0001\u0000\u0000\u000056\u0007\u000b"+
		"\u0000\u000067\u0007\f\u0000\u000078\u0007\r\u0000\u00008\b\u0001\u0000"+
		"\u0000\u00009:\u0007\u0007\u0000\u0000:;\u0007\u0006\u0000\u0000;\n\u0001"+
		"\u0000\u0000\u0000<=\u0005*\u0000\u0000=\f\u0001\u0000\u0000\u0000>?\u0005"+
		",\u0000\u0000?\u000e\u0001\u0000\u0000\u0000@A\u0005=\u0000\u0000A\u0010"+
		"\u0001\u0000\u0000\u0000BC\u0005!\u0000\u0000CD\u0005=\u0000\u0000D\u0012"+
		"\u0001\u0000\u0000\u0000EF\u0005<\u0000\u0000F\u0014\u0001\u0000\u0000"+
		"\u0000GH\u0005>\u0000\u0000H\u0016\u0001\u0000\u0000\u0000IJ\u0005<\u0000"+
		"\u0000JK\u0005=\u0000\u0000K\u0018\u0001\u0000\u0000\u0000LM\u0005>\u0000"+
		"\u0000MN\u0005=\u0000\u0000N\u001a\u0001\u0000\u0000\u0000OQ\u0007\u000e"+
		"\u0000\u0000PO\u0001\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000RP\u0001"+
		"\u0000\u0000\u0000RS\u0001\u0000\u0000\u0000S\u001c\u0001\u0000\u0000"+
		"\u0000TX\u0005\'\u0000\u0000UW\b\u000f\u0000\u0000VU\u0001\u0000\u0000"+
		"\u0000WZ\u0001\u0000\u0000\u0000XV\u0001\u0000\u0000\u0000XY\u0001\u0000"+
		"\u0000\u0000Y[\u0001\u0000\u0000\u0000ZX\u0001\u0000\u0000\u0000[\\\u0005"+
		"\'\u0000\u0000\\\u001e\u0001\u0000\u0000\u0000]a\u0007\u0010\u0000\u0000"+
		"^`\u0007\u0011\u0000\u0000_^\u0001\u0000\u0000\u0000`c\u0001\u0000\u0000"+
		"\u0000a_\u0001\u0000\u0000\u0000ab\u0001\u0000\u0000\u0000b \u0001\u0000"+
		"\u0000\u0000ca\u0001\u0000\u0000\u0000df\u0007\u0012\u0000\u0000ed\u0001"+
		"\u0000\u0000\u0000fg\u0001\u0000\u0000\u0000ge\u0001\u0000\u0000\u0000"+
		"gh\u0001\u0000\u0000\u0000hi\u0001\u0000\u0000\u0000ij\u0006\u0010\u0000"+
		"\u0000j\"\u0001\u0000\u0000\u0000\u0005\u0000RXag\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}